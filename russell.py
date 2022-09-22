def boxes(widgets):
    """
    Puts 280 widgets into 1 box. 
    """
    widgets = (int)(widgets)
    boxes_containing_280_widgets = 0
    
    if widgets >= 280:
        boxes_containing_280_widgets = widgets // 280 #Uses floor division to round down to get exact number of boxes

    if widgets % 280 != 0:
        boxes_containing_280_widgets = boxes_containing_280_widgets + 1 #For the last box that has less then 280 widgets

    return boxes_containing_280_widgets

def main():
    print(boxes(5346)) # returns 20


main()
        
