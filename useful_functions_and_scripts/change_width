# Function for changing seaborn barplot width 

def change_width(ax, new_value) :

    for patch in ax.patches :
    
        current_width = patch.get_width()
        
        diff = current_width - new_value

        # Change the bar width
        patch.set_width(new_value)

        # Recenter the bar
        patch.set_x(patch.get_x() + diff * .5)
