# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



    # Use a breakpoint in the code line below to debug your script.



# Press the green button in the gutter to run the script.
from codrone_edu.drone import Drone

my_drone=Drone()








class tricks:
    def sqaureone(self):

        my_drone.pair()

        my_drone.takeoff()

        power = 40

        my_drone.set_pitch(power)

        my_drone.move(.6)

        my_drone.set_pitch(0)

        my_drone.set_roll(power)

        my_drone.move(.6)

        my_drone.set_roll(0)

        my_drone.set_pitch(-power)

        my_drone.move(.6)

        my_drone.set_pitch(0)

        my_drone.set_roll(-power)

        my_drone.move(.6)

        my_drone.set_roll(0)

        my_drone.land()

        my_drone.close()





    def sqauretwo(self):

        my_drone.pair()

        my_drone.takeoff()

        power = 55

        turn = 52



        for i in range(4):

            my_drone.set_pitch(power)

            my_drone.move(.6)

            my_drone.set_pitch(0)

            my_drone.set_yaw(-turn)

            my_drone.move(.7)

            my_drone.set_yaw(0)

        my_drone.land()

        my_drone.close()




    def circleone(self):

        my_drone.pair()

        my_drone.takeoff()

        power = 100

        my_drone.set_pitch(power)

        my_drone.set_yaw(power)

        for i in range(4):

            my_drone.move(1)

        my_drone.land()

        my_drone.close()



    def wave(self):

        my_drone.pair()

        my_drone.takeoff()

        power = 45

        my_drone.set_pitch(power)

        for i in range(3):

            my_drone.set_throttle(power)

            my_drone.move(.7)

            my_drone.set_throttle(-50)

            my_drone.move(.7)

        my_drone.land()

        my_drone.close()


    def spiral(self):

        my_drone.pair()

        my_drone.takeoff()

        power = 60

        throttle = -60

        turn = 110

        my_drone.set_throttle(30)

        my_drone.move(1.5)

        my_drone.set_throttle(0)

        for i in range(4):

            my_drone.set_throttle(throttle)

            my_drone.set_pitch(power)

            my_drone.set_yaw(turn)

            my_drone.move(.5)

            turn -= 3

            power += 5

            throttle -= 5

        my_drone.land()

        my_drone.close()



    def triangle(self):

        my_drone.pair()

        my_drone.takeoff()

        power = 50

        duration = .8

        turn = -22

        my_drone.set_yaw(turn)

        my_drone.move(duration)

        my_drone.set_yaw(0)

        my_drone.set_pitch(power)

        my_drone.move(duration)

        my_drone.set_pitch(0)

        my_drone.set_yaw(-(turn*2))

        my_drone.move(duration)

        my_drone.set_yaw(0)

        my_drone.set_pitch(-power)

        my_drone.move(duration)

        my_drone.set_pitch(0)

        my_drone.set_yaw(turn)

        my_drone.move(duration)

        my_drone.set_yaw(0)

        my_drone.set_roll(-power)

        my_drone.move(duration)

        my_drone.set_roll(0)

        my_drone.set_pitch(power)

        my_drone.land()

        my_drone.close()



dronetricks = tricks()








class obsticlecourse:



     def courseone(self):

         my_drone.pair()

         my_drone.takeoff()

         power = 34

         my_drone.set_throttle(-44.425)

         my_drone.move(1.425)

         my_drone.set_throttle(0)

         my_drone.set_pitch(power)

         my_drone.move(3.45)

         my_drone.set_pitch(0)

         my_drone.land()

         my_drone.close()


course = obsticlecourse()

if __name__ == '__main__':


 course.courseone()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/











