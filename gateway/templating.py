from jinja2 import Environment, TemplateNotFound, FileSystemLoader

class Templating:
    env: Environment

    def __init__(self):
        self.env = Environment(loader=FileSystemLoader("./gateway/content/templates"))

    def render(self, *, name, args: dict | None = None) -> bytes:
        if args is None:
            args = dict()

        try:
            template = self.env.get_template(f'{name}.html')
        except TemplateNotFound:
            return None
                
        return bytes(template.render(**args), "utf-8")
    
    def error(
        self, 
        *, 
        title: str,
        description: str
    ) -> bytes:
        return self.render(
            name='error', 
            args={
                'title': 'Gateway Error',
                'description': f'Something went wrong while processing your request: {description}',
            }
        )
    
    def error_variant(
        self,
        variant: str,
        *,
        title: str,
        description: str,
        extra: dict
    ) -> bytes:
        return self.render(
            name=f'error/{variant}',
            args={
                'title': title,
                'description': description,
                **extra
            }
        )