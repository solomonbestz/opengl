

def create_2d_world(x_cord: list[int], y_cord: list[int]) -> None:
    for y_cell in range(y_cord[0]+abs(y_cord[1])):
        y_cell =  9 - y_cell
        for x_cell in range(x_cord[0], x_cord[1]+1):
            print((x_cell, y_cell), end="")
        print()




if __name__=='__main__':
    x_cordinates: list[int] = [-9, 9]
    y_cordinates: list[int] = [9, -9]

    create_2d_world(x_cordinates, y_cordinates)