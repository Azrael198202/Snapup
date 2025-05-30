from logger_util import setup_logger
from steps.step1_loader import ExcelLoader
from steps.step2_process import DataProcessor

def main():
    logger = setup_logger()

    logger.info("=== Step 1: Load Excel Data ===")
    loader = ExcelLoader(logger)
    loader.load_all()

    logger.info("=== Step 2: Process Data ===")
    processor = DataProcessor(logger, loader)
    processor.run()

    logger.info("All steps completed.")

if __name__ == '__main__':
    main()
