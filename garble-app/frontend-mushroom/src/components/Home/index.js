import React, { useEffect, useRef, useState } from 'react';
import { withStyles } from '@material-ui/core';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';

import DataService from "../../services/DataService";
import styles from './styles';

const Home = (props) => {
    const { classes } = props;

    console.log("================================== Home ======================================");

    const inputFile = useRef(null);

    // Component States
    const [audio, setAudio] = useState(null);
    const [prediction, setPrediction] = useState(null);

    // Setup Component
    useEffect(() => {

    }, []);

    // Handlers
    const handleAudioUploadClick = () => {
        inputFile.current.click();
    }
    const handleOnChange = (event) => {
        console.log(event.target.files);
        setAudio(URL.createObjectURL(event.target.files[0]));

        var formData = new FormData();
        formData.append("file", event.target.files[0]);
        console.log(formData.get('file'));
        DataService.Predict(formData)
            .then(function (response) {
                console.log(response.data);
                setPrediction(response.data);
            })
    }
    console.log({audio});
    return (
        <div className={classes.root}>
            <main className={classes.main}>
                <Container maxWidth="md" className={classes.container}>
                    {prediction &&
                        <Typography variant="h4" gutterBottom align='center'>
                            {!prediction.poisonous &&
                                <span className={classes.safe}>{prediction.prediction_label + " (" + prediction["accuracy"] + "%)"}</span>
                            }
                            {prediction.poisonous &&
                                <span className={classes.poisonous}>{prediction.prediction_label + " (" + prediction["accuracy"] + "%)"}&nbsp;&nbsp;Poisonous</span>
                            }
                        </Typography>
                    }
                    <div className={classes.dropzone} onClick={() => handleAudioUploadClick()}>
                        <input
                            type="file"
                            accept="audio/*"
                            className={classes.fileInput}
                            ref={inputFile}
                            onChange={(event) => handleOnChange(event)}
                        />
                        <div>{audio && <audio controls src={audio} />}</div>
                        <div className={classes.help}>Click to upload audio file...</div>
                    </div>
                </Container>
            </main>
        </div>
    );
};

export default withStyles(styles)(Home);