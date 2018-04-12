def ethree_colors(x):
    ethree_hex = ["#024e6e", "#af7e00", "#ae2200", "#007e34", "#1abdc5", "#74ce4b"]
    return ethree_hex[x]

def stock_veh_colors(x, vtype):
    qual_hex = ["#e6550d", "#fd8d3c", "#fdae6b", "#fdd0a2", "#3182bd", "#6baed6", "#9ecae1", "#c6dbef",
                "#31a354", "#74c476", "#a1d99b", "#c7e9c0", "#756bb1", "#9e9ac8",
                "#bcbddc", "#dadaeb", "#636363", "#969696", "#bdbdbd", "#d9d9d9"]

    qual_hex2 = ["#393b79", "#5254a3", "#6b6ecf", "#9c9ede", "#637939", "#8ca252", "#b5cf6b",
             "#cedb9c", "#8c6d31", "#bd9e39", "#e7ba52" ,"#e7cb94", "#843c39", "#ad494a",
             "#d6616b", "#e7969c", "#7b4173", "#a55194", "#ce6dbd", "#de9ed6" ]

    if vtype == 'LDV':

        color_dict = {'Reference Gasoline LDV' : qual_hex[3],
                     'SP Gasoline LDV' : qual_hex[2],
                     'Reference PHEV40' : qual_hex[5],
                     'PHEV40' : qual_hex[5],
                     'BEV' : qual_hex[4],
                     'Hydrogen Fuel Cell' : qual_hex[12]}

    if vtype == 'MDV':

        color_dict = {'Reference MDV-Gasoline' : qual_hex[3],
                      'Efficient MDV Gasoline' : qual_hex[2],
                      'Reference MDV-Diesel' : qual_hex[1],
                      'Efficient MDV Diesel' : qual_hex[1],
                      'Diesel Hybrid MDV' : qual_hex[0],
                      'MDV CNG' : qual_hex2[13],
                      'MDV Battery Electric' : qual_hex[4],
                      'MDV Hydrogen FCV' : qual_hex[12]}

    if vtype == 'HDV':

        color_dict = {'Reference Diesel HDV' : qual_hex[1],
                      'Efficient HDV Diesel' : qual_hex[2],
                      'Hybrid Diesel HDV' : qual_hex[1],
                      'Efficient HDV CNG' : qual_hex2[13],
                      'HDV Battery Electric' : qual_hex[4],
                      'HDV Hydrogen FCV' : qual_hex[12]}

    if vtype == 'Bus':
        color_dict = {'Gasoline Bus' : qual_hex[3],
                      'Diesel Bus' : qual_hex[1],
                      'CNG Bus' : qual_hex[13],
                      'BEV Bus' : qual_hex[4]}

    return color_dict[x]
