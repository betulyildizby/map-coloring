import plotly.express as px
import pandas as pds

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]


# Write your code here
# ....................
# ....................
# ....................
# ....................
# ....................

graph = {
    'Argentina': ['Chile', 'Bolivia', 'Paraguay', 'Brazil', 'Uruguay'],
    'Bolivia': ['Peru', 'Brazil', 'Paraguay', 'Argentina', 'Chile'],
    'Brazil': ['Colombia', 'Venezuela', 'Guyana', 'Suriname', 'French Guiana', 'Peru', 'Bolivia', 'Paraguay', 'Argentina', 'Uruguay'],
    'Chile': ['Argentina', 'Bolivia', 'Peru'],
    'Colombia': ['Venezuela', 'Brazil', 'Ecuador', 'Peru'],
    'Ecuador': ['Colombia', 'Peru'],
    'Falkland Islands': [],
    'Guyana': ['Suriname', 'Brazil'],
    'Paraguay': ['Brazil', 'Bolivia', 'Argentina'],
    'Peru': ['Ecuador', 'Colombia', 'Brazil', 'Bolivia', 'Chile'],
    'Suriname': ['French Guiana', 'Brazil'],
    'Uruguay': ['Argentina', 'Brazil'],
    'Venezuela': ['Colombia', 'Brazil', 'Guyana'],     
   
}

# Colors for nodes
colors = {node: None for node in graph}


colors = ["blue", "green", "red", "yellow"]

 
def dfs(node):
    
    used_colors = set(colors[neighbor] for neighbor in graph[node] if colors[neighbor] is not None)
    
    # Unused colors
    unused_colors = colors - used_colors
    
   
    colors[node] = next(iter(unused_colors))
    
    
    for neighbor in graph[node]:
        if colors[neighbor] is None:
            dfs(neighbor)

# DFS
def dfs(node, colors):
    for color in colors:
        if colors(node, color, colors):
            colors[node] = color
            for neighbor in graph[node]:
                dfs(neighbor, colors)
            colors[node] = None

# Pandas DataFrame 
dataframe = pds.DataFrame({'node': list(colors), 'color': list(colors)})

# Showing map 
fig = px.choropleth(dataframe, locations='node', locationmode='country names', color='color', scope='south america')



# Do not modify this method, only call it with an appropriate argument.
# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":


    # coloring test
    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}

    plot_choropleth(colormap=colormap_test)

