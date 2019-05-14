/*
class main {
    public static void main(String[] args) {
        
        //Fork[] f = new Fork[5];
        //for (int i = 0; i < 5; i++) f[i] = new Fork();
        // // following is to prevent deadlock, i.e. need to change order of picking up
        // // fork for last philosopher, they need to pick up the right fork first.
        //for (int i = 0; i < 4; i++) new Philosopher(i, f[i], f[i+1]).start();
        //new Philosopher(4, f[0], f[4]).start();
        

        Table tab = new Table();
        for (int i = 0; i < 5; i++) new Philosopher2(tab, i).start();
    }
}
*/