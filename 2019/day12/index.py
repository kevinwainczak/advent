class Moon:
    def __init__(self, x, y, z):
        self.x_pos = x
        self.y_pos = y
        self.z_pos = z
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0
    
    def __str__(self):
        return 'pos=<x= {}, y={}, z={}>, vel=<x= {}, y={}, z={}>'.format(
            self.x_pos,
            self.y_pos,
            self.z_pos,
            self.x_vel,
            self.y_vel,
            self.z_vel
        )
    
    def add_x_grav(self):
        self.x_vel += 1
    
    def add_y_grav(self):
        self.y_vel += 1
    
    def add_z_grav(self):
        self.z_vel += 1
    
    def sub_x_grav(self):
        self.x_vel -= 1
    
    def sub_y_grav(self):
        self.y_vel -= 1
    
    def sub_z_grav(self):
        self.z_vel -= 1
    
    @staticmethod
    def apply_gravity(moon1, moon2):
        if moon1.x_pos > moon2.x_pos:
            moon2.add_x_grav()
            moon1.sub_x_grav()
        elif moon1.x_pos < moon2.x_pos:
            moon2.sub_x_grav()
            moon1.add_x_grav()
        
        if moon1.y_pos > moon2.y_pos:
            moon2.add_y_grav()
            moon1.sub_y_grav()
        elif moon1.y_pos < moon2.y_pos:
            moon2.sub_y_grav()
            moon1.add_y_grav()
        
        if moon1.z_pos > moon2.z_pos:
            moon2.add_z_grav()
            moon1.sub_z_grav()
        elif moon1.z_pos < moon2.z_pos:
            moon2.sub_z_grav()
            moon1.add_z_grav()

    def apply_velocity(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        self.z_pos += self.z_vel

    def get_kinetic_energy(self):
        return abs(self.x_vel) + abs(self.y_vel) + abs(self.z_vel)

    def get_potential_energy(self):
        return abs(self.x_pos) + abs(self.y_pos) + abs(self.z_pos)

    def get_total_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()
    
    @staticmethod
    def get_system_total_energy(moons):
        total = 0
        for moon in moons:
            total += moon.get_total_energy()
        return total
    
    @staticmethod
    def get_state(moons):
        state = ''
        for moon in moons:
            state += str(moon)
        return state

def apply_grav_pairs(moons):
    for i in range(len(moons)):
        for j in range(i + 1, len(moons)):
            moon1 = moons[i]
            moon2 = moons[j]

            Moon.apply_gravity(moon1, moon2)

def challenge1(steps):
    moons = [
        Moon(-14, -4, -11),
        Moon(-9, 6, -7),
        Moon(4, 1, 4),
        Moon(2, -14, -9)]
    # moons = [
    #     Moon(-1, 0, 2),
    #     Moon(2, -10, -7),
    #     Moon(4, -8, 8),
    #     Moon(3, 5, -1)]
    
    for x in range(steps):
        apply_grav_pairs(moons)
        for moon in moons:
            moon.apply_velocity()
    
    return Moon.get_system_total_energy(moons)

print challenge1(1000)

def challenge2():
    # moons = [
    #     Moon(-14, -4, -11),
    #     Moon(-9, 6, -7),
    #     Moon(4, 1, 4),
    #     Moon(2, -14, -9)]
    moons = [
        Moon(-1, 0, 2),
        Moon(2, -10, -7),
        Moon(4, -8, 8),
        Moon(3, 5, -1)]

    prev_states = set()
    prev_states.add(Moon.get_state(moons))

    steps = 0
    while True:
        if steps % 10000000 == 0:
            print steps
        steps += 1
        apply_grav_pairs(moons)
        for moon in moons:
            moon.apply_velocity()
        state = Moon.get_state(moons)
        if state in prev_states:
            return steps
        prev_states.add(state)

print challenge2()

    