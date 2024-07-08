import { useState } from 'react';
import { AiOutlineFileExcel } from 'react-icons/ai';
import * as XLSX from 'xlsx';
import './dropzoneStyle.css';

const Dropzone = ({ onFileUpload }) => {
  const [fileName, setFileName] = useState(null);

  const handleButtonClick = () => {
    document.getElementById('fileInput').click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      console.log(`Selected file: ${file.name}`);

      const reader = new FileReader();
      reader.onload = (e) => {
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, { type: 'array' });
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        const json = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

        // Extract the first column
        const urls = json.slice(1).map(row => row[0]); // Assuming the first row is the header

        // Output the extracted URLs
        console.log('Extracted URLs:', urls);

        // Call the parent callback with the URLs and file name
        onFileUpload(urls, file.name);
      };
      reader.readAsArrayBuffer(file);
      setFileName(file.name);
    }
  };

  return (
    <div className="w-full">
      <button
        type="button"
        className="relative block w-full rounded-lg border-2 border-dashed border-gray-300 p-16 text-center hover:border-gray-400 focus:outline-none focus:ring-2 focus:ring-gradient focus:ring-offset-2"
        onClick={handleButtonClick}
      >
        <AiOutlineFileExcel className="mx-auto h-16 w-16 text-gray-400" />
        <span className="mt-4 block text-lg font-semibold text-gray-900">
          Drag in your Excel file with reference links
        </span>
      </button>
      <input
        id="fileInput"
        type="file"
        accept=".csv, .xls, .xlsx"
        className="hidden"
        onChange={handleFileChange}
        onClick={(event) => event.target.value = null} // Clear the input value on click to allow re-uploading the same file
      />
    </div>
  );
};

export default Dropzone;
