import Dropzone from '../components/Dropzone/Dropzone';
import Navbar from '../components/nav';
import './style.css';

const Home = () => {
  return (
    <div className="min-h-screen bg-white">
      <Navbar />
      <main className="flex flex-col lg:flex-row items-center lg:items-center justify-center flex-grow mt-20 sm:mt-24 md:mt-32 lg:mt-40 px-8 max-w-7xl mx-auto lg:gap-36">
        <h1 className="text-5xl text-center lg:text-left font-extrabold lg:max-w-md leading-tight font-inter">
          <span className="bg-clip-text text-transparent bg-gradient-to-r from-blue-500 via-cyan-400 to-cyan-200">Reference.</span>
          <br />
          <span className="text-black">AI Summarize.</span>
          <br />
          <span className="text-black">A Single Click</span>
        </h1>
        <div className="flex flex-col items-center lg:items-start mt-12 lg:mt-0">
          <Dropzone />
          <button className="mt-10 px-4 py-2 text-md button-gradient rounded-full lg:self-end lg:ml-auto font-inter font-bold" style={{ borderRadius: "2rem" }}>
            <span>Generate</span>
          </button>
        </div>
      </main>
    </div>
  );
};

export default Home;
