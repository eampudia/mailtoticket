from filtres.reply import FiltreReply
import settings

import logging
logger = logging.getLogger(__name__)

class FiltreReplyReobrint(FiltreReply):

  def filtrar(self):
    logger.info ("El ticket esta [%s]" % self.ticket['estat']);
    if self.ticket['estat']=='TIQUET_STATUS_TANCAT':
        logger.info ("Reobrim el ticket tancat %s" % self.ticket_id);
        resultat=self.tickets.modificar_tiquet(
            codiTiquet=self.ticket_id,
            estat='TIQUET_STATUS_OBERT'
        )
    return FiltreReply.filtrar(self)