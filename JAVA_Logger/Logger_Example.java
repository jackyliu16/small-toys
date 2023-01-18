public class Logger_Example {
  static final Logger log = Logger.INSTANCE;
  public static void main(String[] args) {
    System.out.println("Normal Output");
    System.out.println("===== ===== ===== =====");
    testLog();
    log.setLogLevel(LogLevel.Debug);
    System.out.println("===== ===== ===== =====");
    testLog();
    log.setLogLevel(LogLevel.Error);
    System.out.println("===== ===== ===== =====");
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
