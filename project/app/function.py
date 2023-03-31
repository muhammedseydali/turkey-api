def generate_auto_id(model):
    last_id = model.objects.order_by('-auto_id').first()
    if last_id:
        return last_id.auto_id + 1
    else:
        return 1
