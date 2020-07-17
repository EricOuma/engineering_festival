from django import template

register = template.Library()


@register.filter(name='crop')
def crop_cloudinary_image(value):
    """crops the image by scaling down"""
    return value.build_url(width=343, height=373, crop='scale')


@register.filter(name='face_thumbnail')
def face_thumbnail(value):
    """crops the image to a square while focusing on the face"""
    return value.build_url(width=150, height=150, gravity="face", radius="max", crop="thumb")