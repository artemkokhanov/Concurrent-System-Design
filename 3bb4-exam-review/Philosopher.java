class Philosopher extends Thread {
    int i;
    Fork first;
    Fork second;
    
    Philosopher(int i, Fork first, Fork second) {
        this.i = i;
        this.first = first;
        this.second = second;
    }
    
    public void run() {
        while (true) {
            try {
                // locking System.out for printing produces better output
                synchronized (System.out) {System.out.println(i + " is thinking");}
                Thread.sleep(100); // milliseconds
                first.pickup();
                second.pickup();
                synchronized (System.out) {System.out.println(i + " is eating");}
                Thread.sleep(100); // milliseconds
                first.putdown();
                second.putdown();
            } catch (Exception e) {System.out.println("something went wrong");}
        }
    }
    
}
