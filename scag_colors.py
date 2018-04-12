def gen_color(gen_tech):

    gen = ['Wind', 'Solar', 'Nuclear', 'Geothermal', 'Hydro', 'Rooftop PV', 'Biomass', 'CHP', 'Imports', 'Coal', 'Natural Gas' ]
    gencolors = ['#8dd3c7','#fed976','#bebada','#fb8072','#80b1d3','#fdb462','#b3de69','grey','#d9d9d9','darkgrey','silver']

    gen_color_dict = dict(zip(gen, gencolors))

    return gen_color_dict[gen_tech]

def scenario_colors(scenario, scag = False):
    #colors = ['dimgrey','#377eb8','#4daf4a','thistle','#ff7f00']
    #colors = ['darkgrey', '#80b1d3','#8dd3c7',  '#fb8072', '#bebada', ]
    scag_colors = ['grey', '#0BA2D1', '#37AB59', '	#B190C5', '#F57F1E']
    colors = ['grey', '#386cb0',  '#7fc97f','#8dd3c7', '#beaed4',]
    scenarios = ['Reference', 'Building Electrification', 'High Biofuels', 'SB 350 Plus', 'Moderate VMT']
# building electrification colors #ff7f00, '#386cb0'
    if scag == False:
        scenario_colors = dict(zip(scenarios, colors))
    if scag == True:
        scenario_colors = dict(zip(scenarios, scag_colors))

    return scenario_colors[scenario]

def bldgs_color_picker(end_uses):

    qual_hex2 = ["#393b79", "#5254a3", "#6b6ecf", "#9c9ede", "#637939", "#8ca252", "#b5cf6b",
      "#cedb9c", "#8c6d31", "#bd9e39", "#e7ba52" ,"#e7cb94", "#843c39", "#ad494a",
     "#d6616b", "#e7969c", "#7b4173", "#a55194", "#ce6dbd", "#de9ed6" ]

    qual_hex = ["#e6550d", "#fd8d3c", "#fdae6b", "#fdd0a2", "#3182bd", "#6baed6", "#9ecae1", "#c6dbef",
            "#31a354", "#74c476", "#a1d99b", "#c7e9c0", "#756bb1", "#9e9ac8",
            "#bcbddc", "#dadaeb", "#636363", "#969696", "#bdbdbd", "#d9d9d9" ]

    reds = ['#fee391','#fec44f','#fe9929','#ec7014','#cc4c02','#8c2d04']
    blues = ['#d0d1e6','#a6bddb','#74a9cf','#3690c0','#0570b0','#034e7b']
    purples = ['#bfd3e6','#9ebcda','#8c96c6','#8c6bb1','#88419d','#6e016b']

    qual_hex3 = ['#fee391','#fec44f','#fe9929','#ec7014','#cc4c02','#8c2d04',
                 '#d0d1e6','#a6bddb','#74a9cf','#3690c0','#0570b0','#034e7b',
                 '#bfd3e6','#9ebcda','#8c96c6','#8c6bb1','#88419d','#6e016b']

#    qual_hex3 = reds + blues[::-1] + purples

    output = []
    gas_counter = 0
    elec_counter = 0
    other_counter = 0
    for end_use in end_uses:

        if 'gas' in end_use.lower() or 'lpg' in end_use.lower():
            output.append(qual_hex3[gas_counter + 6])
            gas_counter +=1

        elif 'electric' in end_use.lower():
            output.append(qual_hex3[elec_counter + 0])
            elec_counter += 1

        elif 'no' in end_use.lower():
            output.append('grey')

        else:
            output.append(qual_hex3[::-1][other_counter + 1])
            other_counter += 1

    return output

def veh_fuel_colors(vehicle):
    veh_stock = {'Efficient HDV Diesel' : '#d95f02',
             'Efficient MDV Diesel' : '#d95f02',
             'Reference Diesel HDV' : '#d95f02',
             'Reference MDV-Diesel' : '#d95f02',
             'Diesel Bus' : '#d95f02',
             'Efficient HDV CNG' : '#8da0cb',
             'CNG Bus' : '#8da0cb',
             'MDV CNG' : '#8da0cb',
             'Efficient MDV Gasoline' : 'black',
             'HDV Hydrogen FCV' : '#7570b3',
             'MDV Hydrogen FCV' : '#7570b3',
             'Hydrogen Fuel Cell' : '#7570b3',
             'Hybrid Diesel HDV' : '#a6761d',
             'Diesel Hybrid MDV' : '#a6761d',
             'PHEV40' : '#a6761d',
             'Reference PHEV40' : '#a6761d',
             'HDV Battery Electric' : '#e6ab02',
             'MDV Battery Electric' : '#e6ab02',
             'BEV' : '#e6ab02',
             'BEV Bus' : '#e6ab02',
             'Reference MDV-Gasoline' : '#666666',
             'Reference Gasoline LDV' : '#666666',
             'Gasoline Bus' : 'red',
             'SP Gasoline LDV' : 'blue',
             'SP Gasoline LDV' : '#666666'
                                    }
    return veh_stock[vehicle]

def veh_type_colors(vehicle):

    veh_cols = {'Aviation': '#fb9a99',
                 'Buses': '#33a02c',
                 'Freight Rail': '#b2df8a',
                 'Harborcraft': '#1f78b4',
                 'Heavy Duty Trucking': '#ff7f00',
                 'Light Duty Vehicles': '#cab2d6',
                 'Medium Duty Trucking': '#fdbf6f',
                 'Ocean Going Vessels': '#a6cee3',
                 'Passenger Rail': '#e31a1c'}

    return veh_cols[vehicle]

def final_fuel_colors(fuel):
    fuel_col = {'Compressed Pipeline Gas (CNG)': '#8da0cb',
                'Natural Gas' : '#8da0cb',
                'RNG' : '#c7e9c0',
                 'Diesel': '#d95f02',
                 'Renewable Diesel' : '#74c476',
                 'Electricity': '#e6ab02',
                 'Gasoline': '#666666',
                 'Renewable Gasoline' : '#31a354',
                 'Hydrogen': '#7570b3',
                 'Kerosene-Jet Fuel': '#a6761d',
                 'Other' : '#d9d9d9'}

    return fuel_col[fuel]
