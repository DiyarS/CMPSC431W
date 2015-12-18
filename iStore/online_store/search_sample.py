def search_description(query):
    items_to_output = []
    for item in Items.objects.all():
        arr = item.description.split()
        for string in arr:
            if string == query:
                items_to_output.append(item)
                break 

    return items_to_output