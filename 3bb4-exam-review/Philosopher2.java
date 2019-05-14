class Philosopher2 extends Thread {
    Table t;
    int ph;
    
    Philosopher2(Table t, int ph) {
        this.t = t;
        this.ph = ph;
    }
    
    public void run() {
        while (true) {
            try {
                synchronized (System.out) {System.out.println(ph + " is thinking");}
                Thread.sleep(100);
                t.pickup(ph);
                synchronized (System.out) {System.out.println(ph + " is eating");}
                Thread.sleep(100);
                t.putdown(ph);
            } catch (Exception e) {System.out.println(ph + " something went wrong");}
        }
    }
    
}