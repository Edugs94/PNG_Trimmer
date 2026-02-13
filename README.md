# PNG Asset Trimmer ✂️ 🖼️ ✂️

## Description
A standalone Python utility designed to automatically remove excess transparent padding from PNG images inside the `trim` folder. This tool uses a "hard trim" algorithm that analyzes the alpha channel and applies an opacity threshold to ensure perfectly cropped assets.

## Instructions

1.  **Preparation**: Place your PNG files inside the `trim/` directory at the root of the project.

2.  **Run**: Execute the following command to set up the environment and trim the images automatically:
    ```bash
    make
    ```
    *(This will create the `.venv`, install dependencies, and process the images in one go)*.

3.  **Cleanup**: To remove the virtual environment and cache files:
    ```bash
    make clean
    ```

## Technical Details
* **Target Folder**: Hardcoded to `trim/`.
* **Virtual Environment**: Uses `.venv` for dependency isolation.
* **Algorithm**: Detects pixels with alpha < 10 as transparent and crops the bounding box accordingly.