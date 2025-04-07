import React, { useEffect, useState } from 'react';
import getSpeakers from '../../../services/speakerAPI';

const ViewSpeakers = () => {
  const [speakers, setSpeakers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const fetchSpeakers = async () => {
    try {
      const speakerData = await getSpeakers();
      setSpeakers(speakerData);
      setIsLoading(false);
    } catch (error) {
      setError(error.mesaage);
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchSpeakers();
  }, []);
};

export default ViewSpeakers;
