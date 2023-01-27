;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

class CTProcessor:
    def __init__(self):
        pass

    def dicom_to_nrrd(self, dicom_path, nrrd_path):
        # Read the DICOM image
        image = sitk.ReadImage(dicom_path)

        # Write the image to NRRD format
        sitk.WriteImage(image, nrrd_path)

    def dicom_series_to_nrrd(self, dicom_folder_path, nrrd_path):
        reader = sitk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(dicom_folder_path)
        reader.SetFileNames(dicom_names)
        image = reader.Execute()
        sitk.WriteImage(image, nrrd_path)

    def create_mask(self, image, lower_threshold, upper_threshold):
        # Convert the image to a numpy array
        image_array = sitk.GetArrayFromImage(image)

        # Create a binary mask using the threshold range
        mask = (image_array > lower_threshold) & (image_array < upper_threshold)

        # Convert the mask back to a SimpleITK image
        mask_image = sitk.GetImageFromArray(mask.astype(int))
        return mask_image

    def apply_mask(self, image, mask):
        # Convert the image and mask to numpy arrays
        image_array = sitk.GetArrayFromImage(image)
        mask_array = sitk.GetArrayFromImage(mask)

        # Apply the mask to the image
        masked_image_array = np.where(mask_array, image_array, 0)

        # Convert the masked image back to a SimpleITK image
        masked_image = sitk.GetImageFromArray(masked_image_array)
        return masked_image
