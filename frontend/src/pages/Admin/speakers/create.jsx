import React, { useState } from 'react';
// import axios from 'axios';
import { Box, TextField, Button, Typography, Input } from '@mui/material';
import speakerAPI from '../../../services/speakerAPI';
import ModalError from '../../../components/Common/modalError';
import ModalSuccess from '../../../components/Common/modalSuccess';

const CreateSpeaker = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    company: '',
    position: '',
    bio: '',
    speaker_avatar: null,
  });

  // Modal state
  const [errorOpen, setErrorOpen] = useState(false);
  const [successOpen, setSuccessOpen] = useState(false);
  const [apiMessage, setApiMessage] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleFileChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      speaker_avatar: e.target.files[0],
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new FormData();
    data.append('name', formData.name);
    data.append('email', formData.email);
    data.append('company', formData.company);
    data.append('position', formData.position);
    data.append('bio', formData.bio);
    data.append('speaker_avatar', formData.speaker_avatar);

    console.log(data);

    // try {
    //   const response = await speakerAPI.addSpeaker(data);
    //   console.log('Speaker created:', response.data);
    //   alert('Speaker successfully registered!');
    // } catch (error) {
    //   console.error('Error creating speaker:', error);
    //   alert('Failed to register speaker.');
    // }
    try {
      const response = await speakerAPI.addSpeaker(data);
      console.log('Speaker created:', response.data);
      setApiMessage('Speaker successfully registered!');
      setSuccessOpen(true);
    } catch (error) {
      console.error(
        'Error creating speaker:',
        error.response ? error.response.data : error.message
      );

      // Catch correct backend error field
      const backendError = error.response?.data?.error || 'Failed to register speaker.';
      setApiMessage(backendError);
      setErrorOpen(true);
    }
  };

  return (
    <Box
      component="form"
      onSubmit={handleSubmit}
      sx={{
        display: 'flex',
        flexDirection: 'column',
        gap: 2,
        width: '400px',
        margin: 'auto',
        mt: 5,
      }}
    >
      <Typography variant="h4" textAlign="center" mb={2}>
        Register Speaker
      </Typography>

      <TextField name="name" label="Name" value={formData.name} onChange={handleChange} required />

      <TextField
        name="email"
        label="Email"
        type="email"
        value={formData.email}
        onChange={handleChange}
        required
      />

      <TextField
        name="company"
        label="Company"
        value={formData.company}
        onChange={handleChange}
        required
      />

      <TextField
        name="position"
        label="Position"
        value={formData.position}
        onChange={handleChange}
        required
      />

      <TextField
        name="bio"
        label="Bio"
        multiline
        rows={4}
        value={formData.bio}
        onChange={handleChange}
        required
      />

      <Input
        type="file"
        name="speaker_avatar"
        onChange={handleFileChange}
        inputProps={{ accept: 'image/*' }}
        required
      />

      <Button variant="contained" type="submit">
        Submit
      </Button>

      <ModalError open={errorOpen} handleClose={() => setErrorOpen(false)} message={apiMessage} />

      <ModalSuccess
        open={successOpen}
        handleClose={() => setSuccessOpen(false)}
        message={apiMessage}
      />
    </Box>
  );
};

export default CreateSpeaker;
