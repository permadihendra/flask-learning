import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import App from './App';

// Newly Added
import { createBrowserRouter, RouterProvider, Navigate } from 'react-router';
import HomePage from './pages/HomePage/HomePage';
import AboutPage from './pages/AboutPage/AboutPage';
import SpeakerPage from './pages/SpeakerPage/SpeakerPage';
import SpeakerDetail from './pages/SpeakerDetail/SpeakerDetail';
import EventsPage from './pages/EventsPage/EventsPage';
import SponsorsPage from './pages/SponsorsPage/SponsorsPage';
import ContactPage from './pages/ContactPage/ContactPage';
import LoginPage from './pages/LoginPage/LoginPage';
import SignUp from './pages/Auth/SignUp';

// Import AdminPage Component
import AdminPage from './pages/Admin/AdminPage/AdminPage';
import Speakers from './pages/Admin/AdminPage/Speakers';
import Dashboard from './pages/Admin/AdminPage/Dashboard';
import ViewSpeakers from './pages/Admin/speakers/page';

// Router/Routing
const router = createBrowserRouter([
  {
    path: '/',
    element: <HomePage />,
  },

  {
    path: '/admin',
    element: <AdminPage />,
    children: [
      {
        index: true, // ✅ Default route
        element: <Navigate to="/admin/dashboard" replace />,
      },
      {
        path: '/admin/dashboard',
        element: <Dashboard />,
      },
      {
        path: '/admin/speakers',
        element: <ViewSpeakers />,
      },
      //   {
      //     path: "/admin/venues",
      //     element: <venues />,
      //   },
      //   {
      //     path: "/admin/events",
      //     element: <Events />,
      //   },
      //   {
      //     path: "/admin/schedules",
      //     element: <Schedules />,
      //   },
      //   {
      //     path: "/admin/sponsors",
      //     element: <Sponsors />
      //   }
    ],
  },

  {
    path: '/about',
    element: <AboutPage />,
  },
  {
    path: '/speakers',
    children: [
      {
        index: true,
        element: <SpeakerPage />,
      },
      {
        path: '/speakers/:speakerId',
        element: <SpeakerDetail />,
      },
    ],
  },
  {
    path: '/events',
    element: <EventsPage />,
  },
  {
    path: '/sponsors',
    element: <SponsorsPage />,
  },
  {
    path: '/contact',
    element: <ContactPage />,
  },

  {
    path: '/auth/login',
    element: <LoginPage />,
  },
  {
    path: '/auth/signup',
    element: <SignUp />,
  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<RouterProvider router={router} />);
