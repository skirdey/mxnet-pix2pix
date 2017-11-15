from __future__ import print_function
import logging


class Trainer(object):
    logging.basicConfig(level=logging.INFO)

    def __init__(self, trainee, options=None):
        assert trainee
        assert options
        self.opts = options
        self.trainee = trainee
        self.epochs = options.max_epochs if options.max_epochs else 400
        self.checkpoint_every_epoch = options.checkpoint_freq
        self.resume = options.resume_training if options.resume_training else False
        self.resume_epoch = options.resume_epoch if options.resume_epoch else 0

    def save_progress(self, epoch):
        self.trainee.save_progress(epoch)

    def resume_progress(self, epoch):
        self.trainee.resume_progress(epoch)

    def setup_network(self):
        self.trainee.setup()

    def do_train(self):

        if self.resume:
            self.resume_progress(self.resume_epoch)
        else:
            self.setup_network()

        for epoch in range(0, self.epochs):

            self.trainee.run_iteration()

            if epoch % self.checkpoint_every_epoch == 0:
                print(epoch)
                self.save_progress(epoch)
