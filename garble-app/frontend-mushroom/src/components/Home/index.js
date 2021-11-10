import React, { useEffect, useRef, useState } from 'react';
import { withStyles } from '@material-ui/core';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';

import DataService from "../../services/DataService";
import styles from './styles';

const SummaryText = ({summary}) => {

  if (summary) { 
    return <div>{summary.summary}</div>
  } else { 
    return <div>No audio file uploaded yet.</div>
  }
}

const Home = (props) => {
  const { classes } = props;

  console.log("================================== Home ======================================");

  const inputFile = useRef(null);

  // Component States
  const [audio, setAudio] = useState(null);
  const [summary, setSummary] = useState(null);
  const [isLoading, setIsLoading] = useState(false); 

  // Setup Component
  useEffect(() => {

  }, []);

  // Handlers
  const handleAudioUploadClick = () => {
    inputFile.current.click();
  }
  const handleOnChange = async (event) => {
    setIsLoading(true);
    console.log(event.target.files);
    setAudio(URL.createObjectURL(event.target.files[0]));

    var formData = new FormData();
    formData.append("file", event.target.files[0]);
    console.log(formData.get('file'));
    await DataService.Predict(formData)
      .then(function (response) {
        console.log('DataService Predict response');
        console.log(response.data);
        setSummary(response.data);
      }); 
    setIsLoading(false);
  }

  return (
    <div className={classes.root}>
      <main className={classes.main}>
        <Container maxWidth="md" className={classes.container}>
          <Grid container spacing={2}>
            <Grid item xs={6}>
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
            </Grid>
            <Grid item xs={6}>
              {isLoading ? <div>Processing</div> : <SummaryText summary={summary} />}
            </Grid>
          </Grid>
        </Container>
      </main>
    </div>
  );
};

export default withStyles(styles)(Home);