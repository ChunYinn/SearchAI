import { Disclosure } from '@headlessui/react';
import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline';
import logo from "../../assets/1.png";

const Navbar = () => {
  return (
    <Disclosure as="nav" className="bg-white border-b">
      {({ open }) => (
        <>
          <div className="max-w-7xl mx-auto flex justify-between items-center py-4 px-8">
            <div className="flex justify-between items-center w-full lg:w-auto">
              <div className="logo">
                <img src={logo} alt="RefMate Logo" className="w-14 md:w-16 lg:w-20" />
              </div>
              <div className="lg:hidden">
                <Disclosure.Button className="text-gray-600 hover:text-black focus:outline-none focus:text-black">
                  <span className="sr-only">Open main menu</span>
                  {open ? (
                    <XMarkIcon className="block h-8 w-8" aria-hidden="true" />
                  ) : (
                    <Bars3Icon className="block h-8 w-8" aria-hidden="true" />
                  )}
                </Disclosure.Button>
              </div>
            </div>
            <div className="hidden lg:flex lg:items-center lg:space-x-10 text-gray-600 text-lg font-bold">
              <a href="#" className="cursor-pointer hover:text-black lg:hover:text-black lg:hover:scale-105 transition-transform duration-200 font-inter">Reference Tool</a>
              <a href="#" className="cursor-pointer hover:text-black lg:hover:text-black lg:hover:scale-105 transition-transform duration-200 font-inter">Feature</a>
              <a href="#" className="cursor-pointer hover:text-black lg:hover:text-black lg:hover:scale-105 transition-transform duration-200 font-inter">About</a>
              <a href="#" className="cursor-pointer hover:text-black lg:hover:text-black lg:hover:scale-105 transition-transform duration-200 font-inter">Feedback</a>
            </div>
          </div>

          <Disclosure.Panel className="lg:hidden">
            <div className="space-y-1 pb-3 pt-2 text-gray-600 text-lg font-bold">
              <Disclosure.Button
                as="a"
                href="#"
                className="block border-l-4 border-transparent py-2 pl-3 pr-4 hover:border-gray-300 hover:bg-gray-50 hover:text-gray-700 font-inter"
              >
                Reference Tool
              </Disclosure.Button>
              <Disclosure.Button
                as="a"
                href="#"
                className="block border-l-4 border-transparent py-2 pl-3 pr-4 hover:border-gray-300 hover:bg-gray-50 hover:text-gray-700 font-inter"
              >
                Feature
              </Disclosure.Button>
              <Disclosure.Button
                as="a"
                href="#"
                className="block border-l-4 border-transparent py-2 pl-3 pr-4 hover:border-gray-300 hover:bg-gray-50 hover:text-gray-700 font-inter"
              >
                About
              </Disclosure.Button>
              <Disclosure.Button
                as="a"
                href="#"
                className="block border-l-4 border-transparent py-2 pl-3 pr-4 hover:border-gray-300 hover:bg-gray-50 hover:text-gray-700 font-inter"
              >
                Feedback
              </Disclosure.Button>
            </div>
          </Disclosure.Panel>
        </>
      )}
    </Disclosure>
  );
};

export default Navbar;
