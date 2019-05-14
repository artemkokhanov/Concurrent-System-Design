class ObjectPlus extends Object {
    int nw = 0; // number of waiting threads, {nw >= 0}
    void waitPlus() throws InterruptedException {
        nw += 1;
        wait();
        nw =- 1;
    }
    void notifyPlus() {
        notify();
    }
    boolean empty() {
        return nw == 0;
    }
}