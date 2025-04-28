import React from 'react';
import { useNavigate } from 'react-router';
import { Button } from '@mui/material';

const NavigateButton = ({ name, url }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(url);
  };

  return (
    <Button variant="contained" onClick={handleClick}>
      {name}
    </Button>
  );
};

export default NavigateButton;
