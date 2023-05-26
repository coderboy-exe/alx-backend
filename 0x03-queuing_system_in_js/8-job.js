const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array")
  };

  jobs.map((j) => {
    const job = queue.create('push_notification_code_3', j).save( (err) => {
	if (!err) {
	  console.log('Notification job created:', job.id)
	}
  });

  job.on('complete', (result) => {
    console.log(`Notification job ${job.id} completed`);

  }).on('failed', (error) => {
    console.log(`Notification job ${job.id} failed`);

  }).on('progress', (progress, data) => {
    console.log(`Notificaton job ${job.id} ${progress}% complete`);

  });
});
}

export default createPushNotificationsJobs;
