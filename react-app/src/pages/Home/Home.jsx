import React, { useState } from 'react';
import Dropzone from '../components/Dropzone/Dropzone';
import Navbar from '../components/nav';
import { AiOutlineDelete } from 'react-icons/ai';
import './style.css';

const handleGenerateClick = async (urls) => {
  try {
    const response = await fetch('http://localhost:8000/generateclick', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        data: urls,
      }),
    });
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

const Home = () => {
  const [urls, setUrls] = useState([]);
  const [fileName, setFileName] = useState(null);

  const handleFileUpload = (uploadedUrls, uploadedFileName) => {
    setUrls(uploadedUrls);
    setFileName(uploadedFileName);
  };

  const handleFileRemove = () => {
    setUrls([]);
    setFileName(null);
  };

  return (
    <div className="min-h-screen bg-white">
      <Navbar />
      <main className="flex flex-col lg:flex-row items-center lg:items-center justify-center flex-grow mt-20 sm:mt-24 md:mt-32 lg:mt-40 px-8 max-w-7xl mx-auto lg:gap-36">
        <h1 className="text-5xl text-center lg:text-left font-extrabold lg:max-w-md leading-tight font-inter">
          <span className="bg-clip-text text-transparent bg-gradient-to-r from-blue-500 via-cyan-400 to-cyan-200">
            Reference.
          </span>
          <br />
          <span className="text-black">AI Summarize.</span>
          <br />
          <span className="text-black">A Single Click</span>
        </h1>
        <div className="flex flex-col items-center lg:items-start mt-12 lg:mt-0">
          <Dropzone onFileUpload={handleFileUpload} />
          <div className="flex flex-col sm:flex-row items-center justify-between mt-10 w-full">
            {fileName ? (
              <div className="flex items-center mb-4 sm:mb-0">
                <span className="text-lg font-semibold text-gray-900">{fileName}</span>
                <AiOutlineDelete
                  className="ml-2 h-6 w-auto cursor-pointer text-red-500 hover:text-red-700"
                  onClick={handleFileRemove}
                />
              </div>
            ) : (
              <div className="flex-grow"></div>
            )}
            <button
              className="px-4 py-2 text-md button-gradient rounded-full font-inter font-bold sm:ml-4"
              onClick={() => handleGenerateClick(urls)}
            >
              <span>Generate</span>
            </button>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Home;
