import re
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from django.conf import settings


class ContentLoader:
    def __init__(self, content_dir: Optional[str] = None):
        if content_dir is None:
            content_dir = getattr(settings, 'CONTENT_DIR', 'content')
        
        self.content_dir = Path(settings.BASE_DIR) / content_dir
        self.topics_dir = self.content_dir / 'topics'
    
    def _parse_frontmatter(self, content: str) -> Tuple[Dict, str]:
        metadata = {}
        markdown_content = content
        
        frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
        match = re.match(frontmatter_pattern, content, re.DOTALL)
        
        if match:
            frontmatter_text = match.group(1)
            markdown_content = match.group(2)
            
            for line in frontmatter_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    
                    if value.startswith('[') and value.endswith(']'):
                        value = [v.strip().strip('"').strip("'") 
                                for v in value[1:-1].split(',')]
                    elif value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    elif value.isdigit():
                        value = int(value)
                    
                    metadata[key] = value
        
        return metadata, markdown_content
    
    def load_content(self, file_path: Path) -> Optional[Dict]:
        if not file_path.exists():
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata, markdown_content = self._parse_frontmatter(content)
            
            metadata['file_path'] = str(file_path)
            metadata['content'] = markdown_content
            metadata['slug'] = metadata.get('slug', file_path.stem)
            
            return metadata
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return None
    
    def list_content_files(self, topic: Optional[str] = None) -> List[Path]:
        files = []
        
        if topic:
            topic_path = self.topics_dir / topic
            if topic_path.exists() and topic_path.is_dir():
                files.extend(topic_path.glob('*.md'))
        else:
            if self.topics_dir.exists():
                for topic_dir in self.topics_dir.iterdir():
                    if topic_dir.is_dir():
                        files.extend(topic_dir.glob('*.md'))
                        for subdir in topic_dir.iterdir():
                            if subdir.is_dir():
                                files.extend(subdir.glob('*.md'))
        
        return sorted(files)
    
    def get_content_by_slug(self, slug: str, topic: Optional[str] = None) -> Optional[Dict]:
        files = self.list_content_files(topic=topic)
        
        for file_path in files:
            content = self.load_content(file_path)
            if content and content.get('slug') == slug:
                return content
        
        return None
    
    def get_all_content(self, topic: Optional[str] = None, 
                       status: Optional[str] = None) -> List[Dict]:
        files = self.list_content_files(topic=topic)
        contents = []
        
        for file_path in files:
            content = self.load_content(file_path)
            if content:
                if status is None or content.get('status') == status:
                    contents.append(content)
        
        return contents
    
    def get_roadmap(self, topic: Optional[str] = None) -> Optional[Dict]:
        if topic:
            roadmap_file = self.topics_dir / topic / '_roadmap.md'
        else:
            roadmap_file = self.content_dir / '_roadmap.md'
        
        if not roadmap_file.exists():
            return None
        
        try:
            with open(roadmap_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    yaml_content = parts[1].strip()
                    markdown_content = parts[2].strip()
                    metadata = yaml.safe_load(yaml_content) or {}
                else:
                    metadata = {}
                    markdown_content = content
            else:
                metadata = {}
                markdown_content = content
            
            nodes = metadata.get('nodes', [])
            connections = metadata.get('connections', [])
            
            return {
                'nodes': nodes,
                'connections': connections,
                'metadata': metadata,
                'markdown': markdown_content,
                'topic': topic
            }
        except Exception as e:
            print(f"Error loading roadmap: {e}")
            import traceback
            traceback.print_exc()
            return None

