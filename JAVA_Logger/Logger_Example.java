public class Logger_Example {
  static final Logger log = Logger.INSTANCE;
  public static void main(String[] args) {
    System.out.println("Normal Output");
    System.out.println("===== ===== ===== =====");
    test();
    log.setLogLevel(LogLevel.Debug);
    System.out.println("===== ===== ===== =====");
    test();
    log.setLogLevel(LogLevel.Error);
    System.out.println("===== ===== ===== =====");
    test();
  }

  public static void test() {
    testLog();
  }
  public static void testLog() {
    log.error("error");
    log.warn("warning");
    log.info("info");
    log.debug("debug");
    log.trace("trace");
  }



}
