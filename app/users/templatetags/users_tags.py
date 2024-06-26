from django import template


register = template.Library()

@register.simple_tag()
def get_input_type(label: str) -> str:
    '''
        Кастомный тэг для возврата типа для поля input 
        в соответствии с полем формы
    '''
    
    input_types = {
        'username': 'text',
        'email': 'email',
        'password': 'password',
        'password1': 'password',
        'password2': 'password',
    }
    if res := input_types.get(label.lower()):
        return res
    
    return 'text'