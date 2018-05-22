from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

main_hall = Room("Main Hall")
main_hall.set_description("An astonishing room with a large wooden staircase and ancient art and decorations.")

indoor_garden = Room("Indoor Garden")
indoor_garden.set_description("A fascinating botanical room with various plant life that enriches the room.")

auditorium = Room("Auditorium")
auditorium.set_description("An enormous room with endless seats and a widespread stage")

main_hall.link_room(ballroom, "northwest")
main_hall.link_room(dining_hall, "northeast")
ballroom.link_room(auditorium, "north")
ballroom.link_room(indoor_garden, "west")
ballroom.link_room(main_hall, "southwest")
dining_hall.link_room(kitchen, "west")
dining_hall.link_room(main_hall, "southeast")
kitchen.link_room(indoor_garden, "west")
kitchen.link_room(dining_hall, "east")
indoor_garden.link_room(kitchen, "west")
indoor_garden.link_room(ballroom, "east")
auditorium.link_room(ballroom, "south")



current_room = main_hall          

while True:		
    print("\n")         
    current_room.get_details()         
    command = input("> ")    
    current_room = current_room.move(command)  
