import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import App from './App';

// Newly Added
import { createBrowserRouter, RouterProvider } from 'react-router'
import HomePage from './pages/HomePage/HomePage';
import AboutPage from './pages/AboutPage/AboutPage';
import SpeakerPage from './pages/SpeakerPage/SpeakerPage';
import SpeakerDetail from './pages/SpeakerDetail/SpeakerDetail';
import EventsPage from './pages/EventsPage/EventsPage';
import SponsorsPage from './pages/SponsorsPage/SponsorsPage';
import ContactPage from './pages/ContactPage/ContactPage';
import LoginPage from './pages/LoginPage/LoginPage';
import SignUp from './pages/Auth/SignUp';

// Router/Routing
const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />
  },
  {
    path: "/about",
    element: <AboutPage />,
  },
  {
    path: "/speakers",
    children: [
      {
        index: true,
        element: <SpeakerPage />,
      },
      {
        path: "/speakers/:speakerId",
        element: <SpeakerDetail />
      },
    ],
  },
  {
    path: "/events",
    element: <EventsPage />,
  },
  {
    path: "/sponsors",
    element: <SponsorsPage />,
  },
  {
    path: "/contact",
    element: <ContactPage />,
  },

  {
    path: "/auth/login",
    element: <LoginPage />,
  },
  {
    path: "/auth/signup",
    element: <SignUp />
  }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <RouterProvider router={router} />
);