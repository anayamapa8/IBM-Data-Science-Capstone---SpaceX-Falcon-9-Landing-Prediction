"""
Hands-on Lab: Build an Interactive Dashboard with Plotly Dash

In this lab, you will be building a Plotly Dash application for users to perform interactive visual analytics on SpaceX launch data in real-time.

This dashboard application contains input components such as a dropdown list and a range slider to interact with a pie chart and a scatter point chart. You will be guided to build this dashboard 
application via the following tasks:

    TASK 1: Add a Launch Site Drop-down Input Component
    TASK 2: Add a callback function to render success-pie-chart based on selected site dropdown
    TASK 3: Add a Range Slider to Select Payload
    TASK 4: Add a callback function to render the success-payload-scatter-chart scatter plot

Note:Please take screenshots of the Dashboard and save them. Further upload your notebook to github.

The github url and the screenshots are later required in the presentation slides.

Your completed dashboard application should look like the following screenshot:
"""

"""
After visual analysis using the dashboard, you should be able to obtain some insights to answer the following five questions:

    Which site has the largest successful launches?
    Which site has the highest launch success rate?
    Which payload range(s) has the highest launch success rate?
    Which payload range(s) has the lowest launch success rate?
    Which F9 Booster version (v1.0, v1.1, FT, B4, B5, etc.) has the highest
    launch success rate?
"""

# * COMIENZO, todo en 1 solo paso, leer detalles

"""
# ! TASK 1: Add a Launch Site Drop-down Input Component

We have four different launch sites and we would like to first see which one has the largest success count. Then, we would like to select one specific site and check its detailed success rate (class=0 vs. class=1).

As such, we will need a dropdown menu to let us select different launch sites.

    Find and complete a commented dcc.Dropdown(id='site-dropdown',...) input with following attributes:
        id attribute with value site-dropdown
        options attribute is a list of dict-like option objects (with label and value attributes). You can set the label and value all to be the launch site names in the spacex_df and you need to include the default All option. e.g.,
        value attribute with default dropdown value to be ALL meaning all sites are selected
        placeholder attribute to show a text description about this input area, such as Select a Launch Site here
        searchable attribute to be True so we can enter keywords to search launch sites
"""

"""
# ! TASK 2: Add a callback function to render success-pie-chart based on selected site dropdown

The general idea of this callback function is to get the selected launch site from site-dropdown and render a pie chart visualizing launch success counts.

Dash callback function is a type of Python function which will be automatically called by Dash whenever receiving an input component updates, such as a click or dropdown selecting event.

If you need to refresh your memory about Plotly Dash callback functions, you may refer to the lab you have learned before:

Plotly Dash Lab

Let's add a callback function in spacex_dash_app.py including the following application logic:

    Input is set to be the site-dropdown dropdown, i.e., Input(component_id='site-dropdown', component_property='value')
    Output to be the graph with id success-pie-chart, i.e., Output(component_id='success-pie-chart', component_property='figure')
    A If-Else statement to check if ALL sites were selected or just a specific launch site was selected
        If ALL sites are selected, we will use all rows in the dataframe spacex_df to render and return a pie chart graph to show the total success launches (i.e., the total count of class column)
        If a specific launch site is selected, you need to filter the dataframe spacex_df first in order to include the only data for the selected site. Then, render and return a pie chart graph to show the success (class=1) count and failed (class=0) count for the selected site.

"""

"""
# ! TASK 3: Add a Range Slider to Select Payload

Next, we want to find if variable payload is correlated to mission outcome. From a dashboard point of view, we want to be able to easily select different payload range and see if we can identify some visual patterns.

Find and complete a commented dcc.RangeSlider(id='payload-slider',...) input with the following attribute:

    id to be payload-slider
    min indicating the slider starting point, we set its value to be 0 (Kg)
    max indicating the slider ending point to, we set its value to be 10000 (Kg)
    step indicating the slider interval on the slider, we set its value to be 1000 (Kg)
    value indicating the current selected range, we could set it to be min_payload and max_payload
"""

"""
# ! TASK 4: Add a callback function to render the success-payload-scatter-chart scatter plot

Next, we want to plot a scatter plot with the x axis to be the payload and the y axis to be the launch outcome (i.e., class column). As such, we can visually observe how payload may be correlated with mission outcomes for selected site(s).

In addition, we want to color-label the Booster version on each scatter point so that we may observe mission outcomes with different boosters.

Now, let's add a call function including the following application logic:

    Input to be [Input(component_id='site-dropdown', component_property='value'), Input(component_id="payload-slider", component_property="value")] Note that we have two input components, one to receive selected launch site and another to receive selected payload range
    Output to be Output(component_id='success-payload-scatter-chart', component_property='figure')
    A If-Else statement to check if ALL sites were selected or just a specific launch site was selected
        If ALL sites are selected, render a scatter plot to display all values for variable Payload Mass (kg) and variable class. In addition, the point color needs to be set to the booster version i.e., color="Booster Version Category"
        If a specific launch site is selected, you need to filter the spacex_df first, and render a scatter chart to show values Payload Mass (kg) and class for the selected site, and color-label the point using Boosster Version Category likewise.
"""

#--- HEADER: SPACEX LAUNCH DASHBOARD - COMPLETE APPLICATION
#--- Building an interactive Dash dashboard with dropdown, slider, pie chart, and scatter plot.
#--- This dashboard allows users to explore launch success rates by site and payload mass.

#!--- SECTION 1: IMPORT LIBRARIES
#--- Importing all necessary libraries for data manipulation and dashboard creation.

import pandas as pd                               # Data manipulation and analysis
import dash                                       # Core Dash framework for building web apps
from dash import dcc, html                        # dcc: Dash Core Components (graphs, sliders), html: HTML components
from dash.dependencies import Input, Output       # Input and Output for callback functions
import plotly.express as px                       # Plotly Express for creating interactive charts

#!--- SECTION 2: LOAD AND PREPARE DATA
#--- Loading the SpaceX dataset and creating dropdown options.

# Load the dataset from CSV file
df = pd.read_csv('/home/mapa8/Documents/CIDSPC/MFaD/C10_M3_A_spacex_launch_geo.csv')

# Create dropdown options for launch sites
# Start with 'All Sites' option, then add each unique launch site
options = [{'label': 'All Sites', 'value': 'ALL'}] + [
    {'label': site, 'value': site} for site in df['Launch Site'].unique()
]

#!--- SECTION 3: INITIALIZE DASH APP
#--- Creating the Dash application instance.

app = dash.Dash(__name__)

# * corregida

#!--- SECTION 4: DEFINE APP LAYOUT (CORRECTED)
#--- Structuring the dashboard with HTML and Dash components.

app.layout = html.Div(children=[
    # Page header/title
    html.H1(
        'SpaceX Launch Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}
    ),
    
    # TASK 1: Dropdown
    dcc.Dropdown(
        id='site-dropdown',
        options=options,
        placeholder='Select a Launch Site',
        searchable=True,
        value='ALL'
    ),
    
    # TASK 2: Pie Chart - Use dcc.Graph instead of html.Div
    dcc.Graph(id='success-pie-chart'),
    
    # TASK 3: Payload Range Slider
    html.Div([
        html.P("Payload Range (kg):", style={'fontSize': 16}),
        dcc.RangeSlider(
            id='payload-slider',
            min=0,
            max=10000,
            step=1000,
            marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
            value=[0, 10000]
        )
    ]),
    
    # TASK 4: Scatter Chart - Use dcc.Graph instead of html.Div
    dcc.Graph(id='success-payload-scatter-chart'),
])

#!--- SECTION 5: TASK 2 CALLBACK - PIE CHART
#--- Callback function that updates the pie chart when the dropdown selection changes.
#--- Input: selected launch site from dropdown
#--- Output: pie chart figure

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(selected_site):
    """
    Renders a pie chart showing launch success counts.
    If 'ALL' sites selected: shows total success vs failure for all launches.
    If specific site selected: shows success vs failure for that site only.
    
    Parameters:
        selected_site (str): The value from the dropdown ('ALL' or a site name)
    
    Returns:
        plotly.graph_objects.Figure: A pie chart figure
    """
    # If 'ALL' sites are selected, use all rows in the dataframe
    if selected_site == 'ALL':
        # Group data by Class (1=success, 0=failure) and count occurrences
        # .value_counts() returns a Series with counts for each unique value
        fig = px.pie(
            df, 
            names='class',                     # Column to use for pie segment names
            title='Total Success Launches for All Sites'  # Chart title
        )
    else:
        # If a specific site is selected, filter the dataframe for that site only
        filtered_df = df[df['Launch Site'] == selected_site]
        # Create pie chart for the filtered data
        fig = px.pie(
            filtered_df, 
            names='class',                     # Column to use for pie segment names
            title=f'Success Launches for {selected_site}'  # Chart title with site name
        )
    
    # Return the pie chart figure
    return fig

#* corregida "Replace color='Booster Version Category' with color='Booster Version' in both scatter plots."

#!--- SECTION 6: TASK 4 CALLBACK - SCATTER CHART (CORRECTED)
#--- Callback function that updates the scatter chart when dropdown or slider changes.
#--- Inputs: selected launch site (dropdown), payload range (slider)
#--- Output: scatter chart figure

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id="payload-slider", component_property="value")
    ]
)
def get_scatter_chart(selected_site, payload_range):
    """
    Renders a scatter plot showing Payload Mass vs Class (launch outcome).
    Points are colored by Booster Version.
    
    Parameters:
        selected_site (str): The value from the dropdown ('ALL' or a site name)
        payload_range (list): [min_payload, max_payload] from the slider
    
    Returns:
        plotly.graph_objects.Figure: A scatter chart figure
    """
    # Unpack the payload range from the slider
    low, high = payload_range
    
    # Filter the dataframe based on the payload range
    mask = (df['Payload Mass (kg)'] >= low) & (df['Payload Mass (kg)'] <= high)
    filtered_df = df[mask]
    
    # If 'ALL' sites are selected, use all filtered data
    if selected_site == 'ALL':
        # Create scatter plot for all sites
        # x: Payload Mass (kg), y: class (1=success, 0=failure)
        # color: Booster Version (different colors for different boosters)
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version',          # CORRECTED: 'Booster Version' not 'Booster Version Category'
            title='Payload Mass vs Launch Outcome for All Sites',
            labels={'class': 'Launch Outcome (1=Success, 0=Failure)'}
        )
    else:
        # If a specific site is selected, filter the data for that site only
        site_mask = filtered_df['Launch Site'] == selected_site
        site_filtered_df = filtered_df[site_mask]
        # Create scatter plot for the selected site
        fig = px.scatter(
            site_filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version',          # CORRECTED: 'Booster Version' not 'Booster Version Category'
            title=f'Payload Mass vs Launch Outcome for {selected_site}',
            labels={'class': 'Launch Outcome (1=Success, 0=Failure)'}
        )
    
    # Return the scatter chart figure
    return fig

#!--- SECTION 7: RUN THE APP
#--- Starting the Dash development server.

if __name__ == '__main__':
    app.run(debug=True)  # debug=True enables hot-reloading for faster development