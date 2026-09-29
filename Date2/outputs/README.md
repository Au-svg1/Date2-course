# Weekly Water-Quality Dataset

## Coverage
- Source reports: 33 weekly PDF files.
- Report weeks: 1–33 of 2014.
- Final observation rows: 17,908 (reported missing values are retained).

## Source
China National Environmental Monitoring Centre (中国环境监测总站), national key-section water-quality automatic monitoring weekly reports.

## Reproduction
Open `PDF_Data_Cleaning_and_Dataset_Construction.ipynb` from the Date2 directory and run all cells.

## Processing
Tables were extracted with pdfplumber. Repeated headers were removed using integer station serials; merged labels were carried forward; four indicator columns were reshaped to long format; source tokens and PDF provenance were retained; exact duplicate observations were removed only after logging.

## Known limitations
- Weekly periods are report windows, not verified sampling dates or measurement timestamps.
- Monitoring location type, coordinates, and province are not reliably available and remain missing.
- Reports marked partial or failed in `extraction_log.csv` require manual review; compatible rows remain in the release.
- Availability metrics describe weekly-summary coverage in this local report collection, not daily/hourly instrument completeness.
- Statistical outliers are not automatically measurement errors.
