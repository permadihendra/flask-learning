import React, { useState } from "react";
import axios from "axios";
import "./EventRegistration.css"; // optional custom styles

const EventRegistration = () => {
  const [formValues, setFormValues] = useState({
    first_name: '',
    last_name: '',
    email: '',
    phone: '',
    job_title: '',
    company_name: '',
    company_size: '',
    subject: ''
  });

  const [formErrors, setFormErrors] = useState({});
  const [feedback, setFeedback] = useState('');
  const [status, setStatus] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  // Options for the subject select input
  const OPTIONS = [
    { value: '', label: '' },
    { value: 'React: From First Steps to Professional', label: 'React: From First Steps to Professional' },
    { value: 'A Tour of React Design Patterns', label: 'A Tour of React Design Patterns' },
    { value: 'Web Components', label: 'Web Components' },
    { value: 'Build a Fullstack App from Scratch with Flask and React', label: 'Build a Fullstack App from Scratch with Flask and React' }
  ];

  // ✅ Validate form values
  const validate = (values) => {
    const errors = {};
    if (!values.first_name) errors.first_name = 'First name is required';
    if (!values.last_name) errors.last_name = 'Last name is required';
    if (!values.email) errors.email = 'Email is required';
    if (!values.subject) errors.subject = 'Subject is required';
    return errors;
  };

  // ✅ On input change
  const onChangeHandler = (e) => {
    const { name, value } = e.target;
    setFormValues({ ...formValues, [name]: value });
    setIsSubmitted(false); // prevent feedback showing while typing
  };

  // ✅ On form submit
  const handleSubmit = async (e) => {
    e.preventDefault();

    const errors = validate(formValues);
    setFormErrors(errors);

    if (Object.keys(errors).length > 0) {
      setFeedback("Please fill required fields.");
      setStatus("error");
      setIsSubmitted(true);
      return;
    }

    try {
      const response = await axios.post("/api/v1/events-registration", formValues);

      if (response.data.success) {
        setFeedback("You have successfully registered for this event!");
        setStatus("success");
        setFormValues({  // optional reset
          first_name: '',
          last_name: '',
          email: '',
          phone: '',
          job_title: '',
          company_name: '',
          company_size: '',
          subject: ''
        });
      } else {
        setFeedback("An error occurred: " + response.data.error);
        setStatus("error");
      }
    } catch (error) {
      setFeedback("Server error. Please try again later.");
      setStatus("error");
    }

    setIsSubmitted(true);
  };

  return (
    <div className="section">
      <div className="form-container">
        <h1>Event Attendee Registration</h1>

        <form onSubmit={handleSubmit}>
          {[
            "first_name",
            "last_name",
            "email",
            "phone",
            "job_title",
            "company_name",
            "company_size"

          ].map((field) => (
            <div key={field} className="input-container">
              <label htmlFor={field}>
                {field.replace("_", " ").toUpperCase()}
              </label>
              <input
                id={field}
                name={field}
                type="text"
                value={formValues[field]}
                onChange={onChangeHandler}
              />
              {formErrors[field] && (
                <small className="error">{formErrors[field]}</small>
              )}
            </div>
          ))}

          <div id="input-container" className='input-container'>

          <label htmlFor="subject">Subject</label>

          <select

            id="subject"

            type="subject"

            name="subject"

            value={formValues.subject}

            onChange={onChangeHandler}

          >

            {OPTIONS.map((option) => (

              <option key={option.value} value={option.value}>

                {option.label}

              </option>

            ))}

          </select>

          <p style={{ color: 'red', fontWeight: 'bold' }}>

            {formErrors.subject}

          </p>

          </div>

          <button type="submit">Register</button>

          {isSubmitted && feedback && (
            <div className={`feedback-message ${status}`}>
              {feedback}
            </div>
          )}
        </form>
      </div>
    </div>
  );
};

export default EventRegistration;