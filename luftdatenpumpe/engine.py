# -*- coding: utf-8 -*-
# (c) 2018 Andreas Motl <andreas@hiveeyes.org>
# License: GNU Affero General Public License, Version 3
import logging
from luftdatenpumpe.target import resolve_target_handler

log = logging.getLogger(__name__)


class LuftdatenEngine:

    def __init__(self, kind, targets, dry_run):
        self.kind = kind
        self.targets = targets
        self.dry_run = dry_run

    def process(self, data):

        # Configure target subsystems.
        targets = []
        for target_expression in self.targets:
            log.info('Configuring target {}'.format(target_expression))
            target = resolve_target_handler(target_expression, dry_run=self.dry_run)

            if target is None:
                log.error('Could not resolve target {}'.format(target_expression))
                continue

            if self.kind not in target.capabilities:
                log.warning('Target {} does not handle kind "{}"'.format(target_expression, self.kind))
                continue

            targets.append(target)

        # Emit to active target subsystems.
        item_count = 0
        for item in data:
            for target in targets:
                target.emit(item)
            item_count += 1

        # Signal readyness to each target subsystem.
        for target in targets:
            target.flush()

        log.info('Processed {} records'.format(item_count))