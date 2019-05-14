//%%writefile village.java

class Barber extends Thread {
    BarberShop barberShop;
    Barber(BarberShop s) {
        barberShop = s;
    }
    public void run() {
        while (true) {
            try {
                barberShop.getNextCustomer(); // wait for a customer to sit in the barber's chair
                System.out.println("cutting hair"); Thread.sleep(1000); // milliseconds
                barberShop.finishedCut(); // allow the customer to leave; returns after the customer left
            } catch (InterruptedException e) {}
        }
    }
}

class Customer extends Thread {
    BarberShop barberShop;
    int cust;
    Customer(BarberShop s, int c) {
        barberShop = s; cust = c;
    }
    public void run() {
        while (true) {
            try {
                System.out.println(cust + " lives happily"); Thread.sleep(2000); // milliseconds
                barberShop.getHaircut(cust); // returns after the customer has received a the haircut
            } catch (InterruptedException e) {}
        }
    }
}

class BarberShop {
    int barber = 0;
    int chair = 0;
    int exit = 0;
    // 0 ≤ barber ≤ 1 ∧ 0 ≤ chair ≤ 1 ∧ 0 ≤ exit ≤ 1
    synchronized void getHaircut(int cust) throws InterruptedException {
        System.out.println(cust + " waiting for barber");
        while (barber == 0) wait(); // await barber > 0
        barber -= 1;
        chair += 1; notifyAll(); // chair > 0
        System.out.println(cust + " waiting for exit door");
        while (exit == 0) wait(); // await exit > 0
        exit -= 1 ; notifyAll(); // exit == 0
    }
    synchronized void getNextCustomer() throws InterruptedException {
        // requires barber == 0
        barber += 1; notifyAll(); // barber > 0
        System.out.println("waiting for customer to set in chair");
        while (chair == 0) wait(); // await chair > 0
        chair -= 1;
    }
    synchronized void finishedCut() throws InterruptedException {
        // requires exit == 0
        exit += 1; notifyAll(); // exit > 0
        System.out.println("waiting for barber to leave");
        while (exit > 0) wait(); // await exit == 0
    }
    public static void main(String[] args) {
        //int numCust = Integer.parseInt(args[0]);
        int numCust = 5;
        BarberShop s = new BarberShop();
        new Barber(s).start();
        for (int c = 0; c < numCust; c++) new Customer(s, c).start();
        System.out.println("done");
    }
}