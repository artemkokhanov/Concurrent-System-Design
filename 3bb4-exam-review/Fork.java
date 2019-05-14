class Fork {
    boolean busy = false; // condition variable
    
    synchronized void pickup() throws InterruptedException {
        while (busy) wait(); // if fork gets picked up then wait
        busy = true; // on the first pickup busy = true, then you wait
    }
        
    synchronized void putdown() {
        busy = false; // done with the fork
        notify();
    }
    
}