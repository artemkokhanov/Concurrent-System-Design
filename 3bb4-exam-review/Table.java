class Table {
    boolean[] fork = new boolean[5]; // initially false
    
    synchronized void pickup(int ph) throws InterruptedException {
        int first = (ph < 4 ? ph : 0); // pickup left fork first unless ph = 4
        int second = (ph < 4 ? ph + 1 : 4); // then pickup right unless ph = 4
        while (fork[first]) wait();
        fork[first] = true;
        while (fork[second]) wait();
        fork[second] = true;
    }
    
    synchronized void putdown(int ph) {
        int first = (ph < 4 ? ph : 0);
        int second = (ph < 4 ? ph + 1 : 4);
        fork[first] = false;
        fork[second] = false;
        notifyAll();
    }
    
}