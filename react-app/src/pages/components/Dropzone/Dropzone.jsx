import { useRef } from 'react';
import { AiOutlineFileExcel } from 'react-icons/ai';
import './dropzoneStyle.css';

const Dropzone = () => {
  const fileInputRef = useRef(null);

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      console.log(`Selected file: ${file.name}`);
    }
  };

  return (
    <div>
      <button
        type="button"
        className="relative block w-full rounded-lg border-2 border-dashed border-gray-300 p-16 text-center hover:border-gray-400 focus:outline-none focus:ring-2 focus:ring-gradient focus:ring-offset-2"
        onClick={handleButtonClick}
      >
        <AiOutlineFileExcel className="mx-auto h-16 w-16 text-gray-400" />
        <span className="mt-4 block text-lg font-semibold text-gray-900">Drag in your Excel file with reference links</span>
      </button>
      <input
        type="file"
        accept=".csv, .xls, .xlsx"
        ref={fileInputRef}
        className="hidden"
        onChange={handleFileChange}
      />
    </div>
  );
};

export default Dropzone;
