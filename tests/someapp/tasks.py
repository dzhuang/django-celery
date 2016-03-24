from celery.task import task


@task(name='c.unittest.SomeAppTask')
def SomeAppTask(**kwargs):
    return 42


@task(name='c.unittest.SomeModelTask')
def SomeModelTask(pk):
    from django import VERSION as django_version
    if django_version >= (1, 9):
        from django.apps import apps
        model = apps.get_model('someapp', 'Thing')
    else:
        from django.db.models import get_model
        model = get_model('someapp', 'Thing')
    thing = model.objects.get(pk=pk)
    return thing.name
