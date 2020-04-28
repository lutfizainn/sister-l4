import time

def Pi(num_steps):
    start = time.time()
    step = 1.0/num_steps
    jum = 0
    for i in range(num_steps):
        x= (i+0.5)*step
        jum += (4.0/(1.0+x*x))
    pi = step * jum
    end = time.time()
    print ("Pi with %d steps is %f in %f secs" %(num_steps, pi, end-start))

if __name__ == '__main__':
    Pi(1000)
