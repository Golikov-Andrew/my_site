from django import template

register = template.Library()


def create_class_of_navbar_link_by_title(page_title: str, target_title: str):
    if page_title == target_title:
        return 'navbar-link navbar-link-active'
    return 'navbar-link'


register.filter('create_class_of_navbar_link_by_title',
                create_class_of_navbar_link_by_title)
