import React from "react";
import { useParams } from "react-router";

const SpeakerDetail = () => {

    const {speakerId} = useParams();

    return (
        <div className="page-wrapper">
            <h1>this is SpeakerDetail with the ID: {speakerId} </h1>
        </div>
    );
};

export default SpeakerDetail;