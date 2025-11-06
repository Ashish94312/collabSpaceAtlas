from django.shortcuts import render
from django.http import Http404
from .content_loader import ContentLoader
from .markdown_renderer import render_markdown


def _get_topic_tree():
    try:
        loader = ContentLoader()
    except Exception:
        return []
    
    try:
        topics_dir = loader.topics_dir
        topic_tree = []
        
        if not topics_dir.exists():
            return topic_tree
    except Exception:
        return []
    
    topic_folders = sorted([d for d in topics_dir.iterdir() if d.is_dir() and not d.name.startswith('.')])
    
    for topic_folder in topic_folders:
        topic_name = topic_folder.name.replace('-', ' ').title()
        topic_slug = topic_folder.name
        
        contents = loader.get_all_content(topic=topic_slug)
        content_count = len([c for c in contents if c.get('status') == 'published'])
        
        subtopics = []
        subdirs = sorted([d for d in topic_folder.iterdir() if d.is_dir() and not d.name.startswith('.')])
        
        for subdir in subdirs:
            subtopic_name = subdir.name.replace('-', ' ').title()
            subtopic_slug = f"{topic_slug}/{subdir.name}"
            
            subtopic_contents = loader.get_all_content(topic=subtopic_slug)
            subtopic_count = len([c for c in subtopic_contents if c.get('status') == 'published'])
            
            subtopics.append({
                'name': subtopic_name,
                'slug': subtopic_slug,
                'content_count': subtopic_count
            })
        
        topic_tree.append({
            'name': topic_name,
            'slug': topic_slug,
            'subtopics': subtopics,
            'content_count': content_count
        })
    
    return topic_tree


def content_list(request):
    try:
        loader = ContentLoader()
    except Exception as e:
        import traceback
        traceback.print_exc()
        return render(request, 'collabSpaceAtlas/content_list.html', {
            'contents': [],
            'search_query': '',
            'difficulty_filter': '',
            'topic_slug': None,
            'topic_tree': [],
            'roadmap': None,
            'error': str(e)
        })
    
    search_query = request.GET.get('q', '')
    difficulty_filter = request.GET.get('difficulty', '')
    topic_slug = request.GET.get('topic', None)
    
    try:
        contents = loader.get_all_content(status='published')
    except Exception as e:
        import traceback
        traceback.print_exc()
        contents = []
    
    if topic_slug:
        topic_contents = loader.get_all_content(topic=topic_slug, status='published')
        contents = topic_contents
    
    if search_query:
        filtered_contents = []
        query_lower = search_query.lower().strip()
        for content in contents:
            title = content.get('title', '').lower()
            summary = content.get('summary', '').lower()
            tags = [tag.lower() for tag in content.get('tags', [])]
            if (query_lower in title or 
                query_lower in summary or
                any(query_lower in tag for tag in tags)):
                filtered_contents.append(content)
        contents = filtered_contents
    
    if difficulty_filter:
        contents = [c for c in contents if c.get('difficulty') == difficulty_filter]
    
    topic_tree = _get_topic_tree()
    
    roadmap = None
    roadmap = loader.get_roadmap(topic_slug if topic_slug else None)
    if roadmap:
        import json
        roadmap['nodes_json'] = json.dumps(roadmap['nodes'])
        roadmap['connections_json'] = json.dumps(roadmap['connections'])
    
    context = {
        'contents': contents,
        'search_query': search_query,
        'difficulty_filter': difficulty_filter,
        'topic_slug': topic_slug,
        'topic_tree': topic_tree,
        'roadmap': roadmap,
    }
    return render(request, 'collabSpaceAtlas/content_list.html', context)


def content_view(request, slug):
    loader = ContentLoader()
    
    topic_slug = request.GET.get('topic', None)
    content = loader.get_content_by_slug(slug, topic=topic_slug)
    
    if not content:
        raise Http404("Content not found")
    
    content['html_content'] = render_markdown(content['content'])
    
    roadmap = None
    if topic_slug:
        roadmap = loader.get_roadmap(topic_slug)
    else:
        content_topic = content.get('topic')
        if content_topic:
            roadmap = loader.get_roadmap(content_topic)
    
    next_item = None
    prev_item = None
    
    if roadmap and roadmap.get('nodes') and roadmap.get('connections'):
        nodes = roadmap['nodes']
        connections = roadmap['connections']
        
        graph = {}
        for conn in connections:
            if conn['from'] not in graph:
                graph[conn['from']] = []
            graph[conn['from']].append(conn['to'])
        
        current_node = None
        for node in nodes:
            if node.get('slug') == slug:
                current_node = node
                break
        
        if current_node:
            current_id = current_node.get('id')
            
            if current_id in graph:
                next_ids = graph[current_id]
                if next_ids:
                    next_id = next_ids[0]
                    for node in nodes:
                        if node.get('id') == next_id:
                            next_item = {
                                'title': node.get('label', ''),
                                'slug': node.get('slug', ''),
                                'is_topic': node.get('topic', False)
                            }
                            break
            
            for conn in connections:
                if conn['to'] == current_id:
                    prev_id = conn['from']
                    for node in nodes:
                        if node.get('id') == prev_id:
                            prev_item = {
                                'title': node.get('label', ''),
                                'slug': node.get('slug', ''),
                                'is_topic': node.get('topic', False)
                            }
                            break
                    break
    
    context = {
        'content': content,
        'next_item': next_item,
        'prev_item': prev_item,
        'topic_slug': topic_slug or content.get('topic'),
    }
    return render(request, 'collabSpaceAtlas/content_view.html', context)
