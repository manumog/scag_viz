import warnings
import pandas as pd
import os
from plotly.graph_objs import *

__author__ = 'Manu'


class ScagApp(object):
    """Class contains stock and share information of an application. This is used to generate stock rollover and share
    figures to be displayed on the SCAG website.
    """

    def __init__(self, name, path=os.getcwd(), display_names_dict={}):
        """
        Initializes a SCAG application
        Args:
            name: Name of the application in the csv files e.g. 'HDV' if files are named HDVstocks
            path: Path to take .csv files from (optional)
            display_names_dict: Dictionary mapping technology names to display names in final graphs
        """

        self.appname = name
        self.stock_path = os.path.join(path, self.appname+'stocks.csv')
        share_path = os.path.join(path, self.appname+'shares.csv')

        try:
            self.stock_df = pd.read_csv(self.stock_path, header=[0, 1], index_col=0).fillna(0)
            # 2 header rows, Index col: 1
        except IOError:
            print("{}stock.csv not found in path \n".format(self.name))

        self.shares_present = False
        try:
            self.shares_df = pd.read_csv(share_path, header=[0, 1], index_col=0).fillna(0)
            print(self.shares_df)
            print(self.shares_df.describe())
            # 3 header rows, Index col: 1
            # TODO: Update to include 3 header rows
            self.shares_present = True
            self.shares_years = self.shares_df.index
        except IOError:
            warnings.warn("No shares data found for {}.".format(self.appname))

        # Parsing stock years, scenarios and technologies (NOTE: change this if input csv pattern changes)
        self.stock_years = self.stock_df.index

        self.scenarios = list(self.stock_df.columns.get_level_values(0).unique())
        # Remove unwanted scenarios
        scenarios_to_remove = list()
        scenarios_to_remove.append('SB 350 Reference')
        for scenario in scenarios_to_remove:
            try:
                self.scenarios.remove(scenario)
            except ValueError:
                warnings.warn("{}: Not found in scenarios. No scenarios were removed.".format(scenario))

        self.technologies = list(self.stock_df.columns.get_level_values(1).unique())
        # Remove unwanted technologies
        technologies_to_remove = list()
        for technology in technologies_to_remove:
            try:
                self.technologies.remove(technology)
            except ValueError:
                warnings.warn("{}: Not found in technologies. No technologies were removed.".format(technology))

        # If no display names, use same names are csv
        # TODO: Implement display names
        # if display_names_dict == {}:
        for technology in self.technologies:
            display_names_dict[technology] = technology
        # else:
        #     for tech_name in self.technologies:
        #         self.technology_display_names = display_names_dict[tech_name]

        # Initalize traces and ordered scenarios needed for plotly figures
        self.trace_list, self.ordered_scenarios = self.trace_maker()
        self.updatemenus_output = self.updatemenus(self.ordered_scenarios)

        if self.shares_present:
            # Shares scenarios can be differently named than stocks scenarios
            self.scenarios_shares = list(self.shares_df.columns.get_level_values(0).unique())
            # Remove unwanted scenarios
            scenarios_to_remove = list()
            scenarios_to_remove.append('SB 350 Reference')
            for scenario in scenarios_to_remove:
                try:
                    self.scenarios_shares.remove(scenario)
                except ValueError:
                    warnings.warn("{}: Not found in shares scenarios. No scenarios were removed.".format(scenario))
            # Initalize traces and ordered scenarios needed for plotly figures
            self.trace_list_shares, self.ordered_scenarios_shares = self.trace_maker(
                    df=self.shares_df, scenarios=self.scenarios_shares)
            self.updatemenus_output_shares = self.updatemenus(self.ordered_scenarios_shares)

    def __repr__(self):
        """ Representation of the ScagApp Object
        Returns:
            return_string: Containing application name, scenarios, technologies, start and end year
        """
        return_string = "\nApplication Name: {} \n".format(self.appname)
        return_string += "Scenarios :{} \n".format(self.scenarios)
        return_string += "Technologies: {} \n".format(self.technologies)
        return_string += "Data found from {} to {} \n".format(self.stock_years[0], self.stock_years[-1])
        return return_string

    def trace_maker(self, df=None, scenarios=None, order_yr=2015):
        """
        This function makes traces of each application which are used to plot in plotly
        Args:
            df: Data frame from which traces are made
            scenarios: Scenarios for the trace
            order_yr: The scenarios are ordered based on value in order_yr

        Returns:
            trace_list: List of traces for each scenario
            ordered_scenarios: List of ordered scenarios for each scenario
        """
        if df is None:
            df = self.stock_df
        if scenarios is None:
            scenarios = self.scenarios

        trace_list, ordered_scenarios = list(), list()  # Output from the function

        # Create cumulative data based on order of scenarios
        for scenario in scenarios:
            scenario_data = df[scenario]
            technology_order = list(scenario_data.loc[order_yr].sort_values(ascending=False).index)
            scenario_data = scenario_data[technology_order]
            scenario_data_cumulative = scenario_data.cumsum(1)

            trace_scenario, tech_scenarios = list(), list()  # Temporary holder for each technology within scenario
            for tech in technology_order:
                tech_scenarios.append(scenario)
                trace_scenario.append({'type': 'scatter',
                          'x': self.stock_years,
                          'y': scenario_data_cumulative.get(tech, None),  # TODO: Verify if this is what you want
                          'mode': 'lines',
                          'opacity': 0.7,
                          'name': tech,
                          'hoverinfo': 'x+y',
                          'fill': 'tonexty',
                          'visible': scenario == 'Reference',
                })
            trace_list.append(trace_scenario)
            ordered_scenarios.append(tech_scenarios)

        return trace_list, ordered_scenarios

    def stock_rollover_figure(self):
        """Prints the plotly slider-based plot for the current application's stock
        Returns:
            fig: Plotly figure with layout
        """
        layout = {'title': 'Reference Scenario',   # TODO: Figure out why title is hardcoded here
                  'hovermode': 'closest',
                  'width': 800,
                  'height': 600,
                  'xaxis': {'title': ''},
                  #           'yaxis' : {'title' : 'Vehicles'}, # TODO: Set correct yaxis label
                  'sliders': self.updatemenus_output
                  }
        traces = [trace for trace_scenario in self.trace_list for trace in trace_scenario]
        fig = Figure(data=traces, layout=layout)
        return fig

    def shares_figure(self):
        """Prints the plotly slider-based plot for the current application's shares
        Returns:
            fig: Plotly figure with layout
        """
        layout = {'title': 'Reference Scenario',
                  'hovermode': 'closest',
                  'width': 800,
                  'height': 600,
                  'xaxis': {'title': ''},
                  #           'yaxis' : {'title' : 'Vehicles'}, # TODO: Set correct yaxis label
                  'sliders': self.updatemenus_output_shares
                  }
        traces = [trace for trace_scenario in self.trace_list_shares for trace in trace_scenario]
        fig = Figure(data=traces, layout=layout)
        return fig

    def updatemenus(self, ordered_scenarios):
        """Returns slider stuff that goes into layout
        """

        # Unpack list into single list
        scenarios = [tech_scenario for scenario in ordered_scenarios for tech_scenario in scenario]
        updatemenus_output = list(
            [dict(
                active=0,
                steps=self.slider_steps(scenarios),
                x=0,
                y=0,
                currentvalue={'visible': False}
            ),
            ])
        return updatemenus_output

    @staticmethod
    def slider_steps(scenarios):
        """
        Returns the slider steps to be used in layout of plotly object (used in updatemenus static method)
        Args:
            scenarios: List of scenarios (flattened list)
        Returns:
            steps_list: List of steps used in slider menu
        """
        steps_list = []
        # TODO: Order scenarios so that Reference is first
        for scenario in scenarios:  # TODO: Make display names for each scenario
            step_dict = dict()
            step_dict['label'] = '<b>' + scenario + '</b>'
            step_dict['method'] = 'update'
            step_dict['args'] = [{'visible': [scenario in x for x in scenarios]},
                                 {'title': scenario + ' Scenario'}, ]
            steps_list.append(step_dict)
        return steps_list

