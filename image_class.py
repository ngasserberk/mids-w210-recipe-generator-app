import streamlit as st

#define function for getting list of predictions
def image_class(result, class_names): 
    boxes_list = ['x1','y1','x2','y2','conf','lbl']
    
    #only display ingredients above this conf score
    conf_threshold = 0.15
    
    result_filt = []
    classes = []
    confidences = []
    top_preds = []
    ingred_list = []
    ingred_dict = {}
    
    if 'boxes' in result:
        for i in range(len(result['boxes'])):
            #filter boxes to confidence threshold
            if result['boxes'][i][boxes_list.index('conf')] > conf_threshold:
                result_filt.append(result['boxes'][i])
                img_class = result['boxes'][i][boxes_list.index('lbl')]
                classes.append(img_class)
                confidences.append(result['boxes'][i][boxes_list.index('conf')])
                
        #get ordered list of unique predictions and max confidence
        # Sort and collect top 5 unique class predictions
        raw_preds = sorted(zip(classes, confidences), key=lambda x: x[1], reverse=True)
        seen_classes = set()
        for cls_id, conf in raw_preds:
            if cls_id not in seen_classes:
                top_preds.append((cls_id, conf))
                seen_classes.add(cls_id)
            if len(top_preds) == 5:
                break
    
        for i, (cls_id, conf) in enumerate(top_preds):
            ingred_dict[class_names[int(cls_id)].replace("_", " ")] = conf

    return ingred_dict