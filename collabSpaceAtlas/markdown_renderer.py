import markdown
from markdown.extensions.toc import TocExtension


def render_markdown(content: str) -> str:
    try:
        import pymdownx.arithmatex as arithmatex
        import pymdownx.superfences as superfences
        import pymdownx.emoji as emoji
        import pymdownx.tasklist as tasklist
        import pymdownx.tilde as tilde
    except ImportError:
        extensions = [
            'extra',
            'codehilite',
            'fenced_code',
            'tables',
            'nl2br',
            TocExtension(baselevel=2, toc_depth='2-4'),
        ]
        md = markdown.Markdown(extensions=extensions)
        return md.convert(content)
    
    extensions = [
        'pymdownx.superfences',
        'pymdownx.highlight',
        'pymdownx.inlinehilite',
        'pymdownx.arithmatex',
        'pymdownx.tasklist',
        'pymdownx.tilde',
        'pymdownx.emoji',
        'pymdownx.magiclink',
        'pymdownx.saneheaders',
        'pymdownx.smartsymbols',
        'markdown.extensions.tables',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
        TocExtension(baselevel=2, toc_depth='2-4'),
    ]
    
    extension_configs = {
        'pymdownx.superfences': {
            'custom_fences': [
                {
                    'name': 'mermaid',
                    'class': 'mermaid',
                    'format': superfences.fence_code_format
                }
            ]
        },
        'pymdownx.arithmatex': {
            'generic': True
        },
        'pymdownx.highlight': {
            'use_pygments': True,
            'css_class': 'highlight',
            'linenums': False
        },
        'pymdownx.tasklist': {
            'clickable_checkbox': True
        }
    }
    
    md = markdown.Markdown(
        extensions=extensions,
        extension_configs=extension_configs
    )
    
    html = md.convert(content)
    return html
