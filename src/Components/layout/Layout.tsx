import React from 'react';
import Navigation from './Navigation';
import MusicPlayer from '../MusicPlayer';
import ClickPush from './ClickPush';
import './Layout.css';

interface LayoutProps {
  children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="app-layout">
      <Navigation />
      <main className="main-content">
        {children}
      </main>
      <MusicPlayer />
      <ClickPush />
    </div>
  );
};

export default Layout;