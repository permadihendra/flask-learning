import React from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  Typography,
} from '@mui/material';

const ModalSuccess = ({ open, handleClose, message }) => {
  return (
    <Dialog open={open} onClose={handleClose}>
      <DialogTitle>Success</DialogTitle>
      <DialogContent>
        <Typography color="primary">{message}</Typography>
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose} color="primary" variant="contained">
          OK
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default ModalSuccess;
