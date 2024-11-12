FROM seldonio/mlserver:1.6.1

COPY --chown=mlserver . /opt/mlserver/runtime

RUN pip install /opt/mlserver/runtime

CMD mlserver start /opt/mlserver/runtime
